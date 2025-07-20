import asyncio
from ganglion import context
from ganglion.config import load_config
from ganglion.db import init_db, create_user, create_account
from ganglion.models import Base

async def main():
    """
    Init db and create accounts
    """
    config = load_config("ganglion-local.toml")

    engine = await init_db(config)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await create_account("pod-1", "pod-1", [])    


if __name__ == "__main__":
    asyncio.run(main())