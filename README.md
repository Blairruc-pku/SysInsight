# Sysinsight

## Table of Contents
- [System Overview](#system-overview)
- [Quick Start](#quick-start)
- [Code Structure](#code-structure)
- [Citation](#citation)

## System Overview

SysInsight is a code-driven database tuning system that automatically extracts fine-grained tuning knowledge from DBMS source code to accelerate and stabilize the tuning process. The tuning workflow involves seven steps:

📌 User provides the DBMS to be tuned (e.g., MySQL or PostgreSQL), the target workload, and the optimization objective (e.g., throughput or latency).

📌 SysInsight performs static analysis on DBMS source code using LLVM IR to construct function-knob mappings, identifying which functions are controlled by each configuration parameter through data-flow and control-flow analysis.

📌 SysInsight employs LLM-based code reasoning with iterative AST search to formulate semantic tuning hypotheses, understanding how knobs influence system execution paths and performance implications.

📌 SysInsight conducts hypothesis-guided experimentation and applies customized association rule mining to derive empirically validated tuning rules with explicit conditions, adjustments, and confidence scores.

📌 During online tuning, SysInsight performs system diagnosis using flame graphs and SHAP analysis to identify performance bottleneck functions and selects relevant knobs based on function-knob mappings.

📌 SysInsight retrieves applicable tuning rules and hypotheses matching the current runtime context, then generates configuration recommendations through rule-augmented LLM prompting.

📌 Finally, SysInsight applies the suggested configuration, observes performance feedback, and continuously updates rule statistics to maintain reliability and enable knowledge refinement for future tuning tasks.

## Quick Start
The following instructions assume you are running on Ubuntu 20.04+ and have Python 3.8+ installed:

### Step 1: Clone the Repository
```bash
git clone https://github.com/Blairruc-pku/SysInsight.git
cd SysInsight
```

### Step 2: Install Dependencies
```bash
conda create -n sysinsight python=3.9
conda activate sysinsight
sudo pip install -r requirements.txt
```

### Step 3: Install and Configure Additional Tools

SysInsight leverages Linux perf and other system utilities. Please ensure they are installed:
```bash
sudo apt-get update
sudo apt-get install linux-tools-common linux-tools-generic linux-tools-`uname -r`
```

### Step 4: Install PostgreSQL
```
sudo apt-get update
sudo apt-get install postgresql-14
```

### Step 5: run
```
./run.sh
```

## Code Structure
```
sysinsight/
├── db_configurations/       # Database configuration files
├── DBTuner/                # Database tuning tools
├── Doxypath/               # Documentation generation path
├── FlameGraph/             # Flame graph generation tools
├── HisRule/                # Historical rule engine
├── library/                # Core library files
├── llambo/                 # LLM integration module
├── Results/                # Analysis results output
│   ├── confrence_lat.py    # Conference latency analysis
│   └── confrence_tps.py    # Conference TPS analysis
├── main.py                 # Main program entry point
├── run.sh                 # Launch script

```


## Citation
If you use this codebase, or otherwise found our work valuable, please cite 📒:
```
@article{}
```