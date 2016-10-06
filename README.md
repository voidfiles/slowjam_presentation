% Profiling Python in Production
% Alex Kessinger
% Oct 5, 2016

---

Agenda

- Basics
- Profiling Tools in Python
- Slowjam (It's a tool)

---

Basics

- Profiling
- Monitoring
- Tracing
- Visibility

---

Types of Tools

- Graphs/Events (statsd, ganglia, rrd, cacti)
- Logs
- Profilers

---

[StatsD](https://github.com/etsy/statsd)

- `echo "foo:1|c" | nc -u -w0 127.0.0.1 8125`
- Worry about what you record after the fact
- Very Simple writes
- Many graphing front-ends
- others like this ganglia, cacti, rrd

---

![Grafana](http://grafana.org/assets/img/features/dashboard_ex.png)

---

Logs

- Logstash, FluentD, Scribe, Flume

---

```bash
2010/08/23 15:25:35 [INFO] client: 80.154.42.54, server: localhost, request: "GET /phpmy-admin/scripts/setup.php HTTP/1.1", host: "www.example.com"
2010/08/23 15:25:35 [INFO] client: 80.154.42.54, server: localhost, request: "GET /phpmy-admin/scripts/setup.php HTTP/1.1", host: "www.example.com"
2010/08/23 15:25:35 [INFO] client: 80.154.42.54, server: localhost, request: "GET /phpmy-admin/scripts/setup.php HTTP/1.1", host: "www.example.com"
2010/08/23 15:25:35 [INFO] client: 80.154.42.54, server: localhost, request: "GET /phpmy-admin/scripts/setup.php HTTP/1.1", host: "www.example.com"
```

---

![Kibana](https://www.elastic.co/assets/blt36c3f01e2d1f9048/Screen-Shot-2015-02-17-at-1.55.18-PM1-1024x573.png)

---

Goals

- Why are we writing code?
- How does x support our goal?

---

A General Process For Profiling

- Is it slow?
- Does it affect my goals?

---

Tools I have used (And, will demo)

- [line_profiler](https://github.com/rkern/line_profiler)
- [django-cprofile-middleware](https://github.com/omarish/django-cprofile-middleware)
- [yet-another-django-profiler](https://github.com/safarijv/yet-another-django-profiler)

---

Tools I have not used

- Statistical Profilers
- SnakeViz, RunSnakeRun

---

Demos

---

Slowjam

- Why?

---
