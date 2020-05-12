import bn256

a,_ = bn256.g2_random()
b,_ = bn256.g2_random()
c,_ = bn256.g2_random()

print("\n======== Private keys (a,b,c) ============")
print("a:",a)
print("b:",b)
print("c:",c)

qa = bn256.g2_scalar_base_mult(a)

qb = bn256.g2_scalar_base_mult(b)

qc = bn256.g2_scalar_base_mult(c)

print("\n======== Alice's public key pair ============")

print("Qa: (generated from G2)",qa)

print("\n======== Bob's public key pair ============")

print("Qb: (generated from G2)",qb)

print("\n======== Catherine's public key pair ============")

print("Qc: (generated from G2)",qc)


qa_qb = qa.add(qb)

qa_qc = qa.add(qc)

qb_qc = qb.add(qc)

qa_qb_qc = qa.add(qb_qc)


print("\n======== qa + qb ============")

print("Key1:",qa_qb)

print("\n======== qa + qc ============")

print("Key1:",qa_qc)

print("\n======== qb + qc ============")

print("Key1:",qb_qc)

print("\n======== qa + qb + qc ============")

print("Key1:",qa_qb_qc)
