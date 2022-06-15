# Projeto Final Cloud

O projeto tem como objetivo fazer a arquitetura do "Case: ABC Place" proposto em aula. Onde utilizamos as ferramentas de kubernets e terraform com objetivo de realizar o deploy automatico dessa aplicação.

## Configurando variáveis de ambiente (credenciais AWS):
```console
$ TF_VAR_AWS_ACCESS_KEY_ID="sua access key" TF_VAR_AWS_SECRET_ACCESS_KEY="sua secret_access key"
```

## Aplicando arquitetura Kubernete:
```console
$ terraform plan
$ terraform apply
```

## Efetuando deploy da imagem Docker:
```console
$ cd ./AppDeploy
$ ansible-playbook playbook.yml
```
