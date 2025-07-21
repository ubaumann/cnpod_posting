import asyncio
from ganglion.config import load_config
from ganglion.db import init_db, db_session, create_account  # create_user
from ganglion.cli import app

async def main():
    """
    Init db and create accounts
    """
    
    config = load_config("ganglion-local.toml")

    await init_db(config)
    async with db_session():
        # user = await create_user("name", "email", "password")
        account, api_key = await create_account("pod-1", "pod-1", [])
        print(f"Created account: {account!r}")
        print(f"{api_key.key=}")

if __name__ == "__main__":
    # Call "ganglion initdb"
    app(["initdb"], auto_envvar_prefix="GANGLION", standalone_mode=False)
    
    # Create accounts
    asyncio.run(main())
