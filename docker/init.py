import asyncio
from pathlib import Path
from ganglion.config import load_config
from ganglion.db import init_db, db_session, create_account  # create_user
from ganglion.cli import app

KEY_DIRECTORY = Path(".keys/")


async def main():
    """
    Create API keys (accounts)
    """

    config = load_config("ganglion-local.toml")

    await init_db(config)
    async with db_session():
        # user = await create_user("name", "email", "password")
        account_name = "pod-1"
        account, api_key = await create_account(account_name, account_name, [])
        print(f"Created account: {account!r}")
        print(f"{api_key.key=}")

        key_file = KEY_DIRECTORY / account_name
        with key_file.open("w") as fp:
            fp.write(api_key.key)


if __name__ == "__main__":
    # Call "ganglion initdb"
    app(["initdb"], auto_envvar_prefix="GANGLION", standalone_mode=False)

    # Create accounts
    asyncio.run(main())
