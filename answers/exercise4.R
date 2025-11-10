# Use Ctrl + I to translate some Python code into R code
# Notice that in this script, we do not have the same linter coloring
# as in Python scripts because these are Python code snippets inside
# an R script. However, the chatbot will be able to translate the code.

# Your instruction to the chatbot will be
# I am an experienced Python programmer, and therefore implemented my code in Python.
# However, I have collaborators who prefer R. And, eventually, we will use
# some R packages in this project that are not available in Python.
# Please translate the following Python code into R code.


sieve_eratosthenes <- function(limit) {
    limit <- as.integer(limit)
    if (limit < 2) return(integer(0))
    # vector of length limit+1 where position (n+1) corresponds to number n
    sieve <- rep(TRUE, limit + 1)
    sieve[1:2] <- FALSE  # 0 and 1 are not prime
    r <- floor(sqrt(limit))
    for (p in 2:r) {
        if (sieve[p + 1]) {
            start <- p * p
            idxs <- seq(start, limit, by = p) + 1
            sieve[idxs] <- FALSE
        }
    }
    which(sieve) - 1L
}

sieve_atkin <- function(limit) {
    limit <- as.integer(limit)
    if (limit < 2) return(integer(0))
    sieve <- rep(FALSE, limit + 1) # position (n+1) corresponds to number n
    r <- floor(sqrt(limit))
    for (x in 1:r) {
        xx <- x * x
        for (y in 1:r) {
            yy <- y * y
            n <- 4 * xx + yy
            if (n <= limit && (n %% 12 %in% c(1, 5))) sieve[n + 1] <- !sieve[n + 1]
            n <- 3 * xx + yy
            if (n <= limit && n %% 12 == 7) sieve[n + 1] <- !sieve[n + 1]
            n <- 3 * xx - yy
            if (x > y && n <= limit && n %% 12 == 11) sieve[n + 1] <- !sieve[n + 1]
        }
    }
    primes <- integer(0)
    if (limit >= 2) primes <- c(primes, 2L)
    if (limit >= 3) primes <- c(primes, 3L)
    if (r >= 5) {
        for (i in 5:r) {
            if (sieve[i + 1]) {
                step <- i * i
                for (k in seq(step, limit, by = step)) sieve[k + 1] <- FALSE
            }
        }
    }
    for (i in seq.int(5L, limit)) {
        if (sieve[i + 1]) primes <- c(primes, i)
    }
    primes
}

first_ten_primes_eratosthenes <- function() {
    limit <- 30L
    primes <- sieve_eratosthenes(limit)
    while (length(primes) < 10L) {
        limit <- limit * 2L
        primes <- sieve_eratosthenes(limit)
    }
    primes[1:10]
}

first_ten_primes_atkin <- function() {
    limit <- 30L
    primes <- sieve_atkin(limit)
    while (length(primes) < 10L) {
        limit <- limit * 2L
        primes <- sieve_atkin(limit)
    }
    primes[1:10]
}

# Run and compare
erat_primes <- first_ten_primes_eratosthenes()
atkin_primes <- first_ten_primes_atkin()
cat("Eratosthenes first ten primes:", paste(erat_primes, collapse = " "), "\n")
cat("Atkin       first ten primes:", paste(atkin_primes, collapse = " "), "\n")
cat("Match:", identical(erat_primes, atkin_primes), "\n")
if (!identical(erat_primes, atkin_primes)) stop("The two sieves produced different results")