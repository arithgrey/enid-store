# Dockerfile

FROM node:16.13.2

WORKDIR /frontend

COPY package*.json ./
RUN npm install

COPY . .

CMD ["npm", "run", "dev"]
