#!/bin/bash

cat encoded.txt | \
    base64 -d | \
    base64 -d | \
    base64 -d | \
    base64 -d | \
    base64 -d | \
    base64 -d | \
    base64 -d | \
    base64 -d | \
    base64 -d | \
    base64 -d | \
    base64 -d | \
    base64 -d | \
    base64 -d | \
    base64 -d | \
    base64 -d | \
    base64 -d | \
    uudecode -p
