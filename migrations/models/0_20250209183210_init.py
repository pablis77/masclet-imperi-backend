from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(255) NOT NULL UNIQUE,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "hashed_password" VARCHAR(255) NOT NULL,
    "role" VARCHAR(255) NOT NULL,
    "is_active" BOOL NOT NULL DEFAULT True
);
CREATE INDEX IF NOT EXISTS "idx_users_usernam_266d85" ON "users" ("username");
CREATE INDEX IF NOT EXISTS "idx_users_email_133a6f" ON "users" ("email");
CREATE TABLE IF NOT EXISTS "animals" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "alletar" VARCHAR(255),
    "explotacio" VARCHAR(255),
    "nom" VARCHAR(255) NOT NULL UNIQUE,
    "genere" VARCHAR(255),
    "pare" VARCHAR(255),
    "mare" VARCHAR(255),
    "quadra" VARCHAR(255),
    "cod" VARCHAR(255),
    "num_serie" VARCHAR(255),
    "dob" DATE,
    "estado" VARCHAR(255),
    "part" DATE,
    "genereT" VARCHAR(255),
    "estadoT" VARCHAR(255)
);
CREATE INDEX IF NOT EXISTS "idx_animals_nom_bf4dd6" ON "animals" ("nom");
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
