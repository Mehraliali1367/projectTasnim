## build stage
# FROM node:9.11.1-alpine as build-stage
# WORKDIR /app/
# COPY frontend/package.json /app/
# RUN npm cache verify
# RUN npm install
# COPY frontend /app/
# RUN npm run build

# production stage
FROM nginx
COPY nginx/prod/prod.conf /etc/nginx/nginx.conf
COPY backend/setup/static /usr/src/app/static/
# COPY --from=build-stage /app/dist /dist/
#COPY front/dist /dist/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]