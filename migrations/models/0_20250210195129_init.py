from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "animals" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "nom" VARCHAR(100) NOT NULL UNIQUE,
    "cod" VARCHAR(50)  UNIQUE,
    "num_serie" VARCHAR(50)  UNIQUE,
    "alletar" BOOL NOT NULL  DEFAULT False,
    "estado" VARCHAR(5) NOT NULL  DEFAULT 'ACTIU',
    "genere" VARCHAR(1) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON COLUMN "animals"."estado" IS 'ACTIU: ACTIU\nMORT: MORT';
COMMENT ON COLUMN "animals"."genere" IS 'MASCLE: M\nFEMELLA: F';
CREATE TABLE IF NOT EXISTS "partos" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "fecha" DATE NOT NULL,
    "genere_cria" VARCHAR(1) NOT NULL,
    "estado_cria" VARCHAR(5) NOT NULL  DEFAULT 'ACTIU',
    "numero_parto" INT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "animal_id" INT NOT NULL REFERENCES "animals" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "partos"."genere_cria" IS 'MASCLE: M\nFEMELLA: F';
COMMENT ON COLUMN "partos"."estado_cria" IS 'ACTIU: ACTIU\nMORT: MORT';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
