library(oce)
par(mar=c(3, 3, 1, 1), mgp=c(2, 0.7, 0)) # tighten margins
t <- as.POSIXct("2013-12-1", tz="UTC") + seq(0, 28*24*3600, 3600)
f <- moonAngle(t=t, longitude=-63.6, 
                    latitude=44.65)$illuminatedFraction
plot(t, f, type="l", xlab="Day of 2013", ylab="Moon fraction")
grid()