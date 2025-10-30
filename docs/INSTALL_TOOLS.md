
# **Perf and FlameGraph Installation Guide**

---

## **Perf Installation**

### **On Ubuntu/Debian**

```
sudo apt-get update
sudo apt-get install linux-tools-common linux-tools-generic linux-tools-$(uname -r)
```

### **On CentOS/RHEL**

```
sudo yum install perf
```

### **On Newer RHEL/CentOS Systems**

```
sudo dnf install perf
```

### **Verify Installation**

```
perf --version
perf stat sleep 1
```

---

## **FlameGraph Installation**

```
git clone https://github.com/brendangregg/FlameGraph.git ~/FlameGraph
cd ~/FlameGraph
ls -la
echo 'export PATH=$PATH:'$(pwd) >> ~/.bashrc
source ~/.bashrc
```

---

# **Doxygen Installation and Source Code Analysis**

---

## **Doxygen Installation**

```
sudo apt-get update
sudo apt-get install doxygen graphviz
doxygen --version
```

---

## **Running Doxygen on the Downloaded Source Code**

Modify the three INPUT paths in the Doxyfile (in sysinsight/Doxypath/) according to the locations of your downloaded source code, then run:

```
doxygen Doxyfile
```
