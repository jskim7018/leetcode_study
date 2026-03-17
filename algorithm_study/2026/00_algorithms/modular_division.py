# When MOD is not prime, you cannot use Fermat's Little Theorem.
# Instead, modular division works only if the modular inverse exists, which happens when:
# gcd(a, MOD) = 1

#
# Division requires a multiplicative inverse.
#
# Fermat's Little Theorem:
# If MOD is a prime number and a is not divisible by MOD, then:
# a^(MOD - 1) ≡ 1 (mod MOD)
# therefore
# a^(-1) ≡a^(MOD - 2) (mod MOD)