- [Data Parser](#data-parser)
    - [Download](#download)
        - [In Data](#in-data)
        - [Out Data](#out-data)
    - [CPU Simple](#cpu-simple)
        - [In Data](#in-data-1)
        - [Out Data](#out-data-1)
    - [dd](#dd)
        - [In Data](#in-data-2)
        - [Out Data](#out-data-2)
    - [Web benchmark](#web-benchmark)
        - [In Data](#in-data-3)
        - [Out Data](#out-data-3)
    - [Sysbench](#sysbench)
      - [CPU](#cpu)
        - [In Data](#in-data-4)
        - [Output data](#output-data)
      - [Fileio](#fileio)
        - [In Data](#in-data-5)
        - [Out Data](#out-data-4)
      - [Memory](#memory)
        - [In Data](#in-data-6)
        - [Out Data](#out-data-5)
      - [Threads](#threads)
        - [In Data](#in-data-7)
        - [Out Data](#out-data-6)
    - [Nench](#nench)
        - [In Data](#in-data-8)
        - [Out Data](#out-data-7)

---

# Data Parser
### Download
##### In Data
```
Downloaded 1048576000 bytes in 8.254693 sec
```
##### Out Data
```
[
    {'unit': 'MB/s', 'value': 127.03}
]
```

### CPU Simple
##### In Data
```
0.11916542053222656
```
##### Out Data
```
[
    {'unit': 's', 'value': 0.11916542053222656, 'name': 'mean duration'}
]
```

### dd
##### In Data
```
1000+0 records in
1000+0 records out
512000 bytes (512 kB, 500 KiB) copied, 0.00757135 s, 67.6 MB/s
```
##### Out Data
```
[
    {'unit': 'MB/s', 'value': 67.6}
]
```

### Web benchmark
##### In Data
```
Running 30s test @ http://localhost:8000
  12 threads and 24 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.84s   162.07ms   1.99s    96.82%
    Req/Sec     2.24      3.34    10.00     86.78%
  378 requests in 30.10s, 170.51KB read
  Socket errors: connect 0, read 0, write 0, timeout 1
Requests/sec:     12.56
Transfer/sec:      5.66KB
```
##### Out Data
```
[
    {'unit': 'req/s', 'value': 12.56, 'name': 'requests per second'}
]
```

### Sysbench
#### CPU
##### In Data
```
sysbench 1.0.19 (using bundled LuaJIT 2.1.0-beta2)

Running the test with following options:
Number of threads: 1
Initializing random number generator from current time


Prime numbers limit: 2000

Initializing worker threads...

Threads started!

CPU speed:
    events per second:  7639.29

General statistics:
    total time:                          10.0002s
    total number of events:              76410

Latency (ms):
         min:                                    0.11
         avg:                                    0.13
         max:                                   48.14
         95th percentile:                        0.13
         sum:                                 9881.40

Threads fairness:
    events (avg/stddev):           76410.0000/0.00
    execution time (avg/stddev):   9.8814/0.00
```
##### Output data
```
[
    {
      "unit": "events/s",
      "value": "7639.29",
      "name": "cpu: events per second"
    },
    {
      "unit": "ms",
      "value": "0.13",
      "name": "cpu: avg latency"
    }
]
```

#### Fileio
##### In Data
```
sysbench 1.0.19 (using bundled LuaJIT 2.1.0-beta2)

Running the test with following options:
Number of threads: 1
Initializing random number generator from current time


Extra file open flags: (none)
128 files, 8MiB each
1GiB total file size
Block size 16KiB
Number of IO requests: 0
Read/Write ratio for combined random IO test: 1.50
Periodic FSYNC enabled, calling fsync() each 100 requests.
Calling fsync() at the end of test, Enabled.
Using synchronous I/O mode
Doing random r/w test
Initializing worker threads...

Threads started!


File operations:
    reads/s:                      1221.33
    writes/s:                     814.22
    fsyncs/s:                     2605.62

Throughput:
    read, MiB/s:                  19.08
    written, MiB/s:               12.72

General statistics:
    total time:                          60.0300s
    total number of events:              278495

Latency (ms):
         min:                                    0.00
         avg:                                    0.21
         max:                                   29.84
         95th percentile:                        0.70
         sum:                                59529.68

Threads fairness:
    events (avg/stddev):           278495.0000/0.00
    execution time (avg/stddev):   59.5297/0.00
```
##### Out Data
```
[
    {
      "unit": "reads/s",
      "value": "1221.33",
      "name": "fileio: fileop - read"
    },
    {
      "unit": "writes/s",
      "value": "814.22",
      "name": "fileio: fileop - write"
    },
    {
      "unit": "fsyncs/s",
      "value": "2605.62",
      "name": "fileio: fileop - fsync"
    },
    {
      "unit": "MiB/s",
      "value": "19.08",
      "name": "fileio: throughput - read"
    },
    {
      "unit": "MiB/s",
      "value": "12.72",
      "name": "fileio: throughput - write"
    },
    {
      "unit": "ms",
      "value": "0.21",
      "name": "fileio: avg latency"
    }
]
```

#### Memory
##### In Data
```
sysbench 1.0.19 (using bundled LuaJIT 2.1.0-beta2)

Running the test with following options:
Number of threads: 1
Initializing random number generator from current time


Running memory speed test with the following options:
  block size: 1024KiB
  total size: 10240MiB
  operation: write
  scope: global

Initializing worker threads...

Threads started!

Total operations: 10240 (13193.43 per second)

10240.00 MiB transferred (13193.43 MiB/sec)


General statistics:
    total time:                          0.7740s
    total number of events:              10240

Latency (ms):
         min:                                    0.07
         avg:                                    0.07
         max:                                    0.16
         95th percentile:                        0.08
         sum:                                  758.04

Threads fairness:
    events (avg/stddev):           10240.0000/0.00
    execution time (avg/stddev):   0.7580/0.00

```
##### Out Data
```
[
    {
      "unit": "ops/s",
      "value": "13193.43",
      "name": "memory: totalops per second"
    },
    {
      "unit": "MiB/s",
      "value": "13193.43",
      "name": "memory: speed"
    },
    {
      "unit": "ms",
      "value": "0.07",
      "name": "memory: avg latency"
    }
]
```

#### Threads
##### In Data
```
sysbench 1.0.19 (using bundled LuaJIT 2.1.0-beta2)

Running the test with following options:
Number of threads: 128
Initializing random number generator from current time


Initializing worker threads...

Threads started!


General statistics:
    total time:                          10.1010s
    total number of events:              7567

Latency (ms):
         min:                                    2.81
         avg:                                  169.92
         max:                                  362.29
         95th percentile:                      297.92
         sum:                              1285781.87

Threads fairness:
    events (avg/stddev):           59.1172/0.86
    execution time (avg/stddev):   10.0452/0.03

```
##### Out Data
```
[
    {
      "unit": "ms",
      "value": "169.92",
      "name": "threads: avg latency"
    }
]
```



### Nench
##### In Data
```
-------------------------------------------------
 nench.sh v2019.07.20 -- https://git.io/nench.sh
 benchmark timestamp:    2020-03-20 15:59:33 UTC
-------------------------------------------------

Processor:    Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
CPU cores:    1
Frequency:    2299.860 MHz
RAM:          983M
Swap:         -
Kernel:       Linux 4.15.0-1063-aws x86_64

Disks:
loop0     18M  HDD
loop1     18M  HDD
loop2   91.4M  HDD
loop3   89.1M  HDD
xvda     15G  SSD

CPU: SHA256-hashing 500 MB
    3.224 seconds
CPU: bzip2-compressing 500 MB
    5.426 seconds
CPU: AES-encrypting 500 MB
    1.687 seconds

ioping: seek rate
    min/avg/max/mdev = 179.2 us / 270.9 us / 28.1 ms / 597.4 us
ioping: sequential read speed
    generated 2.74 k requests in 5.01 s, 685.2 MiB, 547 iops, 136.9 MiB/s

dd: sequential write speed
    1st run:    132.56 MiB/s
    2nd run:    120.16 MiB/s
    3rd run:    120.16 MiB/s
    average:    124.30 MiB/s

IPv4 speedtests
    your IPv4:    18.197.105.xxxx

    Cachefly CDN:         92.25 MiB/s
    Leaseweb (NL):        103.32 MiB/s
    Softlayer DAL (US):   8.65 MiB/s
    Online.net (FR):      73.99 MiB/s
    OVH BHS (CA):         14.56 MiB/s

No IPv6 connectivity detected
-------------------------------------------------
```

##### Out Data
```
[
  {
    "unit": "seconds",
    "value": 3.224,
    "name": "cpu - SHA256"
  },
  {
    "unit": "seconds",
    "value": 5.426,
    "name": "cpu - bzip2"
  },
  {
    "unit": "seconds",
    "value": 1.687,
    "name": "cpu - AES"
  },
  {
    "unit": "us",
    "value": 270.9,
    "name": "ioping: avg seek rate"
  },
  {
    "unit": "MiB/s",
    "value": 136.9,
    "name": "ioping: sequential read speed"
  },
  {
    "unit": "MiB/s",
    "value": 124.3,
    "name": "dd: avg sequential write speed"
  },
  {
    "unit": "MiB/s",
    "value": 92.25,
    "name": "net speed - Cachefly CDN"
  },
  {
    "unit": "MiB/s",
    "value": 103.32,
    "name": "net speed - Leaseweb (NL)"
  },
  {
    "unit": "MiB/s",
    "value": 8.65,
    "name": "net speed - Softlayer DAL (US)"
  },
  {
    "unit": "MiB/s",
    "value": 73.99,
    "name": "net speed - Online.net (FR)"
  },
  {
    "unit": "MiB/s",
    "value": 14.56,
    "name": "net speed - OVH BHS (CA)"
  }
]
```

### AI Benchmark
##### In Data
```
{'ai_score': None, 'inference_score': 308, 'training_score': None}
```

##### Out Data
```
[
    {
      "unit": "score",
      "value": 308,
      "name": "inference score"
    }
]
```