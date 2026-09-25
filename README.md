# Caddy mTLS Example

Caddyをリバースプロキシとして配置し、CAを使わずに自己署名クライアント証明書を直接検証するmTLS構成。

## Structure

```text
Client
  │ HTTPS + mTLS :10250
  ▼
Caddy
  │ HTTP :10250
  ▼
Python Server
```

## Caddyfile

```caddyfile
https://localhost:10250 {
    tls /etc/caddy/certs/server/server.crt /etc/caddy/certs/server/server.key {
        client_auth {
            mode require
            verifier leaf {
                folder /etc/caddy/certs/clients
            }
        }
    }

    reverse_proxy hello-server:10250
}
```

## docker-compose.yml

```yaml
services:
  hello-server:
    build: .
    expose:
      - "10250"

  caddy:
    image: caddy:2.11.4-alpine
    depends_on:
      - hello-server
    ports:
      - "10250:10250"
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile:ro
      - ./certs/server:/etc/caddy/certs/server:ro
      - ./certs/clients:/etc/caddy/certs/clients:ro
```

## Notes

主なハマりどころ:

- Caddyが `:10250` で待ち受ける場合、Dockerも `10250:10250` にする。
- CAなしで自己署名クライアント証明書を直接検証する場合は `mode require` を使う。
- `require_and_verify` ではCAチェーン検証が入り、`BAD_CERTIFICATE` になった。
- `verifier leaf` の `folder` では証明書を `.pem` として配置する。
- Docker volumeとCaddyfile内の証明書パスを一致させる。
- `.pem` の追加・削除後はCaddyをreloadする。

```bash
docker compose exec -T caddy \
  caddy reload \
  --config /etc/caddy/Caddyfile \
  --adapter caddyfile \
  --force
```

## Summary

```text
CAなしmTLS
= mode require
+ verifier leaf
+ clients/*.pem
```