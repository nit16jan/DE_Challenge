CREATE TABLE customer
(
customer_id INT NOT NULL,
customer_name VARCHAR(100),
customer_ph_num VARCHAR(100),
customer_address VARCHAR(500),
target_create_dt date, --used to store Record Insert Date
target_update_dt date, --used to store Record Update Date
batch_id int,		       --to help track the batch when record got interted or updated
CONSTRAINT customer_pk PRIMARY KEY (customer_id)
);

CREATE TABLE salesperson
(
person_id INT NOT NULL,
person_name VARCHAR(100),
person_ph_num VARCHAR(100),
person_hire_dt date,
person_termination_dt date,
person_address VARCHAR(500),
target_create_dt date,
target_update_dt date, 
batch_id int, 
CONSTRAINT salesperson_pk PRIMARY KEY (person_id)
);

CREATE TABLE manufacturer
(
manufacturer_id INT NOT NULL,
manufacturer_name VARCHAR(100),
manufacturer_hq_addr VARCHAR(500), 
target_create_dt date,
target_update_dt date, 
batch_id int,
CONSTRAINT manufacturer_pk PRIMARY KEY (manufacturer_id)
);

CREATE TABLE cars
(
car_id INT NOT NULL,
model_name VARCHAR(30),
serial_number INT,
weight real,
price real,
manufacturer_id INT,   --References manufacturer table
target_create_dt date, --used to store Record Insert Date
target_update_dt date, --used to store Record Update Date
batch_id int,		   --to help track the batch when record got interted or updated
CONSTRAINT car_pk PRIMARY KEY (car_id)
);

CREATE TABLE sales
(
sales_id INT NOT NULL,
sales_dt date,
customer_id INT NOT NULL,     --References customer table
salesperson_id INT NOT NULL,  --References salesperson table person_id
car_id INT NOT NULL,          --References car table
quantity INT,
total_price real,
target_create_dt date,
target_update_dt date, 
batch_id int, 
CONSTRAINT sales_pk PRIMARY KEY (sales_id)
);
