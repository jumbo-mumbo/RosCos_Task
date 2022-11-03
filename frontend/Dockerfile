FROM node:slim

RUN npm install -g http-server

WORKDIR /code

COPY . .

RUN npm install

RUN npm run build

EXPOSE 8080

CMD ["http-server", "dist"]