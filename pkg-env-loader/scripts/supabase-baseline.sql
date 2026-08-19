-- Supabase baseline migration for agent-env-loader.
-- Required before first use: supabase db push --file scripts/supabase-baseline.sql
-- Resets RLS and recreates tables for agent credential access.

BEGIN;

ALTER TABLE IF EXISTS auth.users DISABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users can view own data" ON public.profiles;
DROP TABLE IF EXISTS public.profiles CASCADE;
DROP TABLE IF EXISTS public.secrets CASCADE;

CREATE TABLE public.profiles (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT,
  api_key TEXT
);

CREATE TABLE public.secrets (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  value TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE public.profiles DISABLE ROW LEVEL SECURITY;
ALTER TABLE public.secrets DISABLE ROW LEVEL SECURITY;

COMMIT;
