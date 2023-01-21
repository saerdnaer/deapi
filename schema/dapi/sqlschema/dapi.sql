CREATE TABLE places (
	id TEXT PRIMARY KEY,
	url TEXT,
	name TEXT,
	address JSONB
);
COMMENT ON TABLE events IS '@sameAs https://schema.org/Place';

CREATE TABLE organization_legal_form (
		type TEXT PRIMARY KEY,
		title TEXT UNIQUE,
		description TEXT,
		id TEXT
);
COMMENT ON TABLE organization_legal_form IS '@enum';

/*
-- INSERT INTO item_type (type, description) VALUES
		('Episode', 'An episode is a complete video/audio. Episodes can be assigned to seasons or shows.'),
		('EventLivestream', 'An event livestream is a time limited livestream valid for a certain event, e.g. a concert or sport match.'),
		('Section', 'A section is a part of an episode, e.g. a scene of an episode.'),
		('Extra', 'An extra is a special broadcast about another asset and can be used on items or groupings. Extras can be for example trailers, interviews, making-ofs or behind-the-scenes.');
*/


CREATE TABLE organizations (
	id TEXT PRIMARY KEY,
	url TEXT,
	name TEXT,
	title TEXT,
	legal_form TEXT REFERENCES organization_legal_form(type),
	category TEXT,
	description TEXT,
	image JSONB,
	address TEXT,
	mission_statement TEXT,
	founding_date DATE, -- TODO inception? – What about years without day and month?
	founding_location TEXT REFERENCES places(id),
	parent text REFERENCES organizations(id) DEFERRABLE INITIALLY DEFERRED
);
COMMENT ON TABLE events IS '@sameAs https://schema.org/Organization';


CREATE TABLE projects (
	id TEXT PRIMARY KEY,
	url TEXT,
	name TEXT,
	description TEXT,
	image JSONB,
	start_date DATE,
	end_date DATE,
	is_current BOOLEAN
);

CREATE TABLE products (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	image JSONB,
	url TEXT,
	start_date DATE,
	end_date DATE,
	is_current BOOLEAN,
	PRIMARY KEY (id)
);

CREATE TABLE system_domain (
	type TEXT PRIMARY KEY,
	title TEXT UNIQUE,
	description TEXT,
	id TEXT
);
COMMENT ON TABLE system_domain IS '@enum';


CREATE TABLE systems (
	url TEXT PRIMARY KEY,
	domain TEXT REFERENCES system_domain(type),
	name TEXT,
	description TEXT,
	start_date DATE,
	end_date DATE,
	is_current BOOLEAN
);


CREATE TABLE relationship_type (
	type TEXT PRIMARY KEY,
	description TEXT,
	id TEXT
);
COMMENT ON TABLE relationship_type IS '@enum';

CREATE TABLE relationships (
	type TEXT REFERENCES relationship_type(type),
	from_id TEXT NOT NULL,
	to_id TEXT NOT NULL,
	start_date DATE,
	end_date DATE,
	related_to TEXT,
	PRIMARY KEY (from_id, to_id, type)
);


CREATE TABLE concepts (
	type TEXT,
	id TEXT PRIMARY KEY,
	name TEXT,
	description TEXT,
	image JSONB,
	url TEXT,
	PRIMARY KEY (id)
);

CREATE TABLE events (
	type TEXT,
	id TEXT PRIMARY KEY,
	start_date TIMESTAMPTZ NOT NULL,
	end_date TIMESTAMPTZ,
	duration INTERVAL,
	is_current BOOLEAN,
	url TEXT
);
COMMENT ON TABLE events IS '@sameAs https://schema.org/Event';


ALTER TABLE events OWNER TO editor;

