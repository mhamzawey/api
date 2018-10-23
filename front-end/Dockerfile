FROM node:7.8.0

# Override the base log level (info).
ENV NPM_CONFIG_LOGLEVEL warn


RUN mkdir -p /app
WORKDIR /app
COPY package.json /app/package.json
RUN npm install

