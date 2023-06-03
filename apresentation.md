---
marp: true
---
 <!-- theme: uncover-->
![bg opacity](https://th.bing.com/th/id/R.a2f46e02ea8f7f8af6c6989687bd6b52?rik=0keMY0UQso%2b1kg&riu=http%3a%2f%2flogz.io%2fwp-content%2fuploads%2f2016%2f01%2fdocker-facebook.png&ehk=vi9I6O3dyq5d2%2bOmy8ZDLrWQv2LbFNVfkFhTEcajShM%3d&risl=&pid=ImgRaw&r=0)


# Overview do docker


#### O que é o Docker?

Em uma breve definição Docker é uma solução de virtualização. Uma das possiveis formas de criar camadas de abstração.

#### Mas pra virtualização não se tem VMs?

**Sim**, VMs são também uma solução de virtualização. **Porém existem grandes diferenças**.


---
![bg opacity](https://th.bing.com/th/id/R.a2f46e02ea8f7f8af6c6989687bd6b52?rik=0keMY0UQso%2b1kg&riu=http%3a%2f%2flogz.io%2fwp-content%2fuploads%2f2016%2f01%2fdocker-facebook.png&ehk=vi9I6O3dyq5d2%2bOmy8ZDLrWQv2LbFNVfkFhTEcajShM%3d&risl=&pid=ImgRaw&r=0)

# Docker vs VMs

Basicamente os dois criam abstração de camadas.

![w:600 h:300](https://images.contentstack.io/v3/assets/blt300387d93dabf50e/bltb6200bc085503718/5e1f209a63d1b6503160c6d5/containers-vs-virtual-machines.jpg)

VM virtualiza o HW, Docker virtualiza o SO.

---
![bg opacity](https://th.bing.com/th/id/R.a2f46e02ea8f7f8af6c6989687bd6b52?rik=0keMY0UQso%2b1kg&riu=http%3a%2f%2flogz.io%2fwp-content%2fuploads%2f2016%2f01%2fdocker-facebook.png&ehk=vi9I6O3dyq5d2%2bOmy8ZDLrWQv2LbFNVfkFhTEcajShM%3d&risl=&pid=ImgRaw&r=0)

# "Os" Docker

- docker (engine)
- dockerfile
- docker image(*)
- docker-hub(*)
- docker-compose
- docker-swarm
- kubernets

