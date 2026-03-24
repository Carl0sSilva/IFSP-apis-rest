# ⚽ Microsserviços com FastAPI – Comunicação Síncrona

Este projeto demonstra a comunicação síncrona entre dois microsserviços utilizando **FastAPI**, **Docker** e **Docker Compose**.

## 📌 Cenário

Foram implementados dois serviços:

### 🔹 Serviço 1 – Times

* Endpoint: `/times/{id}`
* Retorna dados mockados de um time de futebol

### 🔹 Serviço 2 – Partidas

* Endpoint: `/partidas/{id}`
* Consome o serviço de Times via HTTP

---

## 🛠️ Tecnologias utilizadas

* Python (FastAPI)
* Docker
* Docker Compose
* REST API

---

## ▶️ Como executar o projeto

Clone o repositório:

```bash
git clone (https://github.com/Carl0sSilva/IFSP-apis-rest)
cd IFSP-apis-rest
```

Execute os containers:

```bash
docker compose up --build
```

---

## 🌐 Testando os serviços

### 🔹 Serviço de Times:

http://localhost:8001/times/1

### 🔹 Serviço de Partidas:

http://localhost:8000/partidas/1

---

## ✅ Funcionamento normal

Quando ambos os serviços estão ativos:

![Funcionando](./prints/funcionando.jpg) 
![Funcionando](./prints/funcionandoTimes.jpg)

---

## ❌ Simulação de falha

Para simular falha, o serviço de Times foi interrompido:

```bash
docker stop ms-times
```

Resultado da requisição:

![Falha](./prints/falha.jpg)

---

## 🐢 Simulação de timeout

Foi adicionado um atraso no serviço de Times:

```python
time.sleep(5)
```

Como o timeout da requisição é de 2 segundos, ocorre erro:

![Timeout](./prints/falha.jpg)

---

## 🧠 Análise dos problemas

A comunicação síncrona entre microsserviços pode gerar alguns problemas:

* **Acoplamento forte:** Um serviço depende diretamente do outro
* **Latência:** Cada requisição HTTP aumenta o tempo de resposta
* **Falhas em cascata:** Se um serviço falha, outros também podem falhar
* **Timeout:** Respostas lentas podem causar erro
* **Dependência de rede:** Qualquer instabilidade afeta a comunicação

---

## 🚀 Conclusão

O projeto demonstra como funciona a comunicação síncrona entre microsserviços e evidencia seus principais desafios, como dependência entre serviços, latência e tratamento de falhas.

---
