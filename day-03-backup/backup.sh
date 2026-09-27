#!/bin/bash

set -e

SOURCE_DIR="${1:-$HOME/automation-lab/source}"
BACKUP_DIR="${2:-$HOME/automation-lab/backups}"
ARCHIVE_NAME="backup-$(date +%F-%H%M%S).tar.gz"
ARCHIVE_PATH="$BACKUP_DIR/$ARCHIVE_NAME"

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Source directory does not exist: $SOURCE_DIR"
    exit 1
fi

mkdir -p "$BACKUP_DIR"
tar -czf "$ARCHIVE_PATH" -C "$SOURCE_DIR" .
echo "Backup created: $ARCHIVE_PATH"
