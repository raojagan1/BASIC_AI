# Day 37: Pagination and Filtering

## Goal
Return large event lists in bounded, useful pages.

## Build
Implement `GET /events?page=1&page_size=10&name=file.created`; limit page size to 100.

## Test
Insert 25 events. Page 2 contains no more than 10 records, and a name filter excludes other event types.

## Complete when
Consumers can scan and filter data without downloading everything.