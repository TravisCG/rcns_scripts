
nums <- read.table("nums.csv", sep = "\t", header = F)
X <- c(rep(0,8), rep(1,8), rep(5,8), rep(10,8))
resultmatrix <- data.frame(beta = rep(0, nrow(nums)), tvalue = rep(0, nrow(nums)), rsquare = rep(0, nrow(nums)), pvalue = rep(0, nrow(nums)))

for(i in 1:nrow(nums)){
	inp <- data.frame(Y = as.numeric(nums[i,]), X = X)
	inp[is.na(inp)] <- 0
	model <- lm(Y ~ X, inp)
	res <- summary(model)
	pval <- res$coefficients[2,4]
	beta <- res$coefficients[2,1]
	tval <- res$coefficients[2,3]
	rval <- res$r.squared
	resultmatrix[i,1] <- beta
	resultmatrix[i,2] <- tval
	resultmatrix[i,3] <- rval
	resultmatrix[i,4] <- pval
}

write.table(resultmatrix, "calculated.csv", quote = F, sep = "\t")
