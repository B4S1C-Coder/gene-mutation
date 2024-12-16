This is built on top of the codebase an old project. It is just some modifications built on top of the old codebase and also contains a lot of dead code. However it is advised not to delete / rename any files unless you know what your're doing.

Run the gRPC python server first before running the npm express server

If you are testing with your own .h5 then put it in model_service folder and uncomment the second line and comment the first line in [imagenet.controller.js](backend_service/src/controller/imagenet.controller.js)