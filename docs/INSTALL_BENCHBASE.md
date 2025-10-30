
# **Sysbench Installation

````
sudo yum -y install make automake libtool pkgconfig libaio-devel
sudo yum install sysbench
sysbench --version
````

# **Sysbench Data Preparation**

```
sysbench --db-driver=mysql \
         --mysql-host=127.0.0.1 \
         --mysql-port=3306 \
         --mysql-user=root \
         --mysql-password=Dbiir@500 \
         --mysql-db=sbtest \
         --table_size=80000 \
         --tables=100 \
         --events=0 \
         --threads=150 \
         oltp_read_write prepare \
         > sysbench_prepare.out
```



# **Complete BenchBase Installation and Data Loading Process**

## **Environment Setup and Directory Creation**

```
mkdir ../optimization_results/
mkdir ../optimization_results/temp_results/
mkdir ../optimization_results/$1/
mkdir ../optimization_results/$1/log/

sudo apt-get update
sudo apt-get install git
sudo apt install openjdk-21-jdk

git clone --depth 1 https://github.com/cmu-db/benchbase.git ../benchbase
```

## **BenchBase Build Process**

```
cd ../benchbase
./mvnw clean package -P $1
cd target
tar xvzf benchbase-$1.tgz
cd benchbase-$1
```

## **Data Generation and Loading**

```
java -jar benchbase.jar -b BENCHMARK_NAME -c config/sample_CONFIG.xml --create=true --load=true
```

