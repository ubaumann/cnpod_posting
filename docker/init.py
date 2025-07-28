import os
import asyncio
from pathlib import Path
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from ganglion.config import load_config
from ganglion.db import init_db, db_session, create_account, check_account_slug
from ganglion.models import Account
from ganglion.cli import app

KEY_DIRECTORY = Path(".keys/")
CONFIG_FILE = "ganglion-local.toml"


async def _create_account(account_name: str) -> str:
    account, api_key = await create_account(account_name, account_name, [])
    print(f"Created account: {account!r}")

    return api_key.key


async def _get_api_key(account_name: str, session: AsyncSession) -> str:
    stmt = (
        select(Account)
        .where(Account.slug == account_name)
        .options(selectinload(Account.api_keys))
    )
    result = await session.execute(stmt)
    account = result.scalar_one_or_none()

    if not account:
        raise ValueError(f"Account {account_name} does not exist.")
    if not account.api_keys:
        raise ValueError(f"Account {account_name} has no API keys.")
    return account.api_keys[0].key


async def main():
    """
    Create API keys (accounts)
    """

    config = load_config(CONFIG_FILE)

    await init_db(config)
    async with db_session() as session:
        # user = await create_user("name", "email", "password")
        account_names = os.getenv("ACCOUNTS", "").split(";")
        for account_name in account_names:
            key_file = KEY_DIRECTORY / account_name
            if await check_account_slug(account_name):
                key = await _create_account(account_name)
            elif not key_file.exists():
                key = await _get_api_key(account_name, session)
            else:
                print(
                    f"Account slug '{account_name}' already exists, skipping creation."
                )
                continue

            print(f"Write API key to {key_file}")
            with key_file.open("w") as fp:
                fp.write(key)


if __name__ == "__main__":
    # Call "ganglion initdb"
    app(
        ["initdb", "--config", CONFIG_FILE],
        auto_envvar_prefix="GANGLION",
        standalone_mode=False,
    )

    # Create accounts
    asyncio.run(main())
