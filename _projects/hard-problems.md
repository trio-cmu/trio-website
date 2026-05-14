---
layout: project
permalink: /projects/hard-problems/
title: Global optimization for realistic robotics
subtitle: ...tackling non-convex, non-smooth and long-horizon problems 
description: We push the boundaries of what optimization problems are solvable in robotics, by developing tools based on global optimization.
image: 
- images/projects/hard-problems.png
- images/projects/hard-problems2.png
#external_link: https://github.com/
#repo: greenelab/lab-website-template
order: 1
featured: true
tags:
  - robotics
  - optimization
---

There is always a trade-off between the expressiveness of an optimization problem and the difficulty of solving it. To create more capable robots, we need to push the boundaries of what optimization problems we can solve. For example, explicitly modeling contact interactions instead of using predefined gates and contact sequences can lead to the discovery of more efficient and robust behaviors, using more accurate sensor and noise models leads to better estimation performance, using more accurate dynamics leads to better control performance, and so on. We are actively exploring how to efficiently solve these hard problems in estimation and control, using tools from global optimization.

A main challenge is improving efficiency of solvers and making the modeling aspect more seamless. See our projects on [seamless modeling and optimization](/projects/seamless/) for an overview of our efforts in this direction. 