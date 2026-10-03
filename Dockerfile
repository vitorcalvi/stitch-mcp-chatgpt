FROM node:22-alpine
RUN npm --global install @_davideast/stitch-mcp@0.9.0
USER node
ENTRYPOINT ["stitch-mcp", "proxy"]
