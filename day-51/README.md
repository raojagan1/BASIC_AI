# Day 51: Document Retrieval Index

## Goal
Find relevant knowledge for an AI workflow.

## Build
Split documents into chunks, normalize words, and store an inverted index in SQLite or JSON.

## Test
Query `backup errors`; the document containing both concepts ranks first.

## Complete when
The system retrieves context instead of sending every document to a model.