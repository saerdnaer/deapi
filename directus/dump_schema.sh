#!/bin/sh
pg_dump postgresql://localhost:5432/dapi -n directus > schema.sql
