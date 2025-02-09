from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ALTER COLUMN "username" TYPE VARCHAR(255) USING "username"::VARCHAR(255);
        ALTER TABLE "users" ALTER COLUMN "hashed_password" TYPE VARCHAR(255) USING "hashed_password"::VARCHAR(255);
        ALTER TABLE "users" ALTER COLUMN "role" TYPE VARCHAR(255) USING "role"::VARCHAR(255);
        ALTER TABLE "users" ALTER COLUMN "email" TYPE VARCHAR(255) USING "email"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "pare" TYPE VARCHAR(255) USING "pare"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "alletar" TYPE VARCHAR(50) USING "alletar"::VARCHAR(50);
        ALTER TABLE "animals" ALTER COLUMN "estado" TYPE VARCHAR(50) USING "estado"::VARCHAR(50);
        ALTER TABLE "animals" ALTER COLUMN "estadoT" TYPE VARCHAR(50) USING "estadoT"::VARCHAR(50);
        ALTER TABLE "animals" ALTER COLUMN "explotacio" TYPE VARCHAR(255) USING "explotacio"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "cod" TYPE VARCHAR(50) USING "cod"::VARCHAR(50);
        ALTER TABLE "animals" ALTER COLUMN "genereT" TYPE VARCHAR(50) USING "genereT"::VARCHAR(50);
        ALTER TABLE "animals" ALTER COLUMN "genere" TYPE VARCHAR(50) USING "genere"::VARCHAR(50);
        ALTER TABLE "animals" ALTER COLUMN "nom" TYPE VARCHAR(255) USING "nom"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "mare" TYPE VARCHAR(255) USING "mare"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "quadra" TYPE VARCHAR(50) USING "quadra"::VARCHAR(50);
        ALTER TABLE "animals" ALTER COLUMN "num_serie" TYPE VARCHAR(50) USING "num_serie"::VARCHAR(50);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ALTER COLUMN "username" TYPE VARCHAR(255) USING "username"::VARCHAR(255);
        ALTER TABLE "users" ALTER COLUMN "hashed_password" TYPE VARCHAR(255) USING "hashed_password"::VARCHAR(255);
        ALTER TABLE "users" ALTER COLUMN "role" TYPE VARCHAR(255) USING "role"::VARCHAR(255);
        ALTER TABLE "users" ALTER COLUMN "email" TYPE VARCHAR(255) USING "email"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "pare" TYPE VARCHAR(255) USING "pare"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "alletar" TYPE VARCHAR(255) USING "alletar"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "estado" TYPE VARCHAR(255) USING "estado"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "estadoT" TYPE VARCHAR(255) USING "estadoT"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "explotacio" TYPE VARCHAR(255) USING "explotacio"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "cod" TYPE VARCHAR(255) USING "cod"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "genereT" TYPE VARCHAR(255) USING "genereT"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "genere" TYPE VARCHAR(255) USING "genere"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "nom" TYPE VARCHAR(255) USING "nom"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "mare" TYPE VARCHAR(255) USING "mare"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "quadra" TYPE VARCHAR(255) USING "quadra"::VARCHAR(255);
        ALTER TABLE "animals" ALTER COLUMN "num_serie" TYPE VARCHAR(255) USING "num_serie"::VARCHAR(255);"""
