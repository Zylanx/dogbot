CREATE TABLE IF NOT EXISTS command_statistics (
  command_name text,
  times_used int,
  last_used timestamp without time zone
);

CREATE TABLE IF NOT EXISTS rps_exclusions (
  user_id bigint
);

CREATE TABLE IF NOT EXISTS censorship (
  guild_id bigint,
  enabled text[],
  exceptions bigint[]
);

-- not gonna use arrays here because asyncpg is bad with them
CREATE TABLE IF NOT EXISTS reddit_feeds (
  guild_id bigint,
  channel_id bigint,
  subreddit text
);

CREATE TABLE IF NOT EXISTS tags (
  name text,
  guild_id bigint,
  creator_id bigint,
  value text,
  uses int,
  created_at timestamp without time zone
);
