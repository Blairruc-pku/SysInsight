
# **Database Installation Guide**

We recommend installing databases **from source code**, as later file analysis will require access to the source files.

---

## **PostgreSQL Installation via YUM Repository**

```
sudo yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
sudo yum -qy module disable postgresql
sudo yum install -y postgresql15-server
sudo /usr/pgsql-15/bin/postgresql-15-setup initdb
sudo systemctl start postgresql-15
sudo systemctl enable postgresql-15
sudo systemctl status postgresql-15
```

---

## **PostgreSQL Compilation from Source**

```
sudo yum groupinstall "Development Tools"
sudo yum install readline-devel zlib-devel
wget https://ftp.postgresql.org/pub/source/v15.3/postgresql-15.3.tar.gz
tar -xf postgresql-15.3.tar.gz

cd postgresql-15.3
./configure --prefix=/usr/local/pgsql
make
sudo make install

sudo useradd postgres
sudo mkdir /usr/local/pgsql/data
sudo chown postgres /usr/local/pgsql/data
sudo -u postgres /usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data
```

---

## **MySQL Installation on CentOS**

```
sudo yum update --allowerasing --skip-broken --nobest
sudo wget https://dev.mysql.com/get/mysql80-community-release-el9-3.noarch.rpm
sudo rpm -Uvh https://dev.mysql.com/get/mysql80-community-release-el9-3.noarch.rpm

sudo yum module disable mysql
sudo yum install mysql-community-server --nogpgcheck
mysql --version

sudo systemctl start mysqld.service
systemctl status mysqld
sudo grep 'temporary password' /var/log/mysqld.log
```

---

## **MySQL Source Code Download and Extraction**

```
wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.34.tar.gz
tar -xzf mysql-8.0.34.tar.gz
cd mysql-8.0.34

mkdir build
cd build
cmake .. -DDOWNLOAD_BOOST=1 -DWITH_BOOST=/usr/local/boost \
         -DCMAKE_INSTALL_PREFIX=/usr/local/mysql \
         -DMYSQL_DATADIR=/usr/local/mysql/data \
         -DSYSCONFDIR=/etc

make
sudo make install

sudo useradd mysql
sudo mkdir /usr/local/mysql/data
sudo chown -R mysql:mysql /usr/local/mysql

sudo /usr/local/mysql/bin/mysqld --initialize --user=mysql \
     --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data

sudo /usr/local/mysql/bin/mysqld_safe --user=mysql &

/usr/local/mysql/bin/mysql --version
```

---
