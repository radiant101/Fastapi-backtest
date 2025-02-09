import asyncio
from prisma import Prisma

async def main():
    prisma = Prisma()
    await prisma.connect()
    print("Prisma Client is connected!")
    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())