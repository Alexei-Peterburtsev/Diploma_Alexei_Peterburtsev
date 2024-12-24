#!/bin/bash

cd ..
cd tests

start http://localhost:8089

locust -f locustfile.py --host https://komarovka.by --run-time 10 --autostart --autoquit 10
