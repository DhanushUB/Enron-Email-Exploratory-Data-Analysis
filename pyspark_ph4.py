# importing SparkContext
>>> from pyspark import SparkContext

# reading the .csv format file from the given file path and storing into a dataframe, df
>>> df = spark.read.csv("file:///home/training/desktop")
>>> df.show()

# renaming the columns in the dataset file and stored in df1
>>> columns = ['date','sender_firstname','sender_lastname','receiver','subject','id']
>>> df1 = df.toDF(*columns)
>>> df1.show()

# renaming the data frame to df
>>> df = df.toDF(*columns)
>>> df.show()

# creating and naming the table as data, in which the data from the dataframe will be stored 
>>> sqlContext.registerDataFrameAsTable(df, "data")

# queries to run on the table and store the result 
>>> query1_result=sqlContext.sql("select data.receiver, count(*) as count from data group by receiver order by count desc limit 15")
>>> query2_result=sqlContext.sql("select sender_firstname,sender_lastname, count(*) as count from data group by sender_firstname,sender_lastname order by count desc limit 15")
>>> query3_result=sqlContext.sql("select avg(count) from (select sender_firstname, count(*) as count from data group by sender_firstname order by count desc limit 15")data
>>> query4_result=sqlContext.sql("select receiver, count(*) as count from data group by receiver order by count desc limit 15")
>>> query5_result=sqlContext.sql("select sender_firstname,subject, count(*) AS CountOf from data group by sender_firstname,subject having count(*)>1")

# to show the results on the above queries  
>>> query1_result.show()
>>> query2_result.show()
>>> query3_result.show()
>>> query4_result.show()
>>> query5_result.show()

# some of the trial queries executed on the dataset
>>> spark.sql("select * from data limit 10").show()
>>> df.select("sender").distinct().show()
>>> df.select("sender").show()
