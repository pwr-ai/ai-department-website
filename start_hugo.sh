#!/bin/bash
hugo mod clean
hugo mod get -u
hugo mod tidy
hugo mod vendor
hugo server -D -F -p 8080 -b http://localhost:8080
