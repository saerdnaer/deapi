FROM node:16-alpine

WORKDIR /app

# INSTALL NODEJS DEPENDENCIES
ENV NODE_ENV=production
ADD package.json package-lock.json .npmrc /app/
RUN unset NODE_ENV; npm install --production

ADD . /app/

CMD npm run start
