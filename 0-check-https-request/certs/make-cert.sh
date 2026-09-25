# user1.key, user1.crt, CN=user1 を変更する
# CA: FALSEなため、認証局は存在しない
openssl req -new -x509 \
  -key user1.key \
  -out user1.crt \
  -days 3650 \
  -sha256 \
  -subj "/CN=user1" \
  -addext "basicConstraints=critical,CA:FALSE" \
  -addext "keyUsage=critical,digitalSignature" \
  -addext "extendedKeyUsage=clientAuth"
