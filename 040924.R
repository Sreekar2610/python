5+3
6-5
df<- data.frame(x=c(1,2,3,4,5,6,7),
                y=c(10,20,30,40,50,60,70),
                z=c(100,200,300,400,500,600,700))
df
10%%3
summary(df)
summary(df[,c('x','y')])
sapply(df,sd,na.rm=TRUE)
res<-quantile(df$x,probs=c(0,0.25,0.5,0.75,1))
res
setwd("D:/DATASCIENCE098")
sdata<-read.csv("mtcars.csv",header = TRUE,sep=',')
sdata
summary(sdata)#descriptive statistics of data
View(sdata)#opens the file
str(sdata)#gives structure of file
res<-quantile(sdata$mpg,probs=c(0,0.25,0.5,0.75,1))
res
