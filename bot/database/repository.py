from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.models import Human

class HumanRepository:

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all(self) -> list[Human]:
        result = await self.session.execute(select(Human))
        humans = result.scalars().all()
        return humans

    async def add_human(self, human_data: dict) -> Human:
        
        new_human = Human(**human_data)
        self.session.add(new_human)
        await self.session.commit()
        
        await self.session.refresh(new_human)
        return new_human
