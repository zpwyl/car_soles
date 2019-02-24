
    let scene, camera, renderer, controls, guiControls;

    /* 场景 */
    function initScene() {
        scene = new THREE.Scene();
        var skySphereGeometry = new THREE.SphereGeometry( 500, 30, 100 );
        var texture = new THREE.TextureLoader().load("/static/img/public_img/timg.jpg");
        var skySphereMaterial = new THREE.MeshBasicMaterial( { map:texture, side: THREE.DoubleSide } );
        var skySphere = new THREE.Mesh( skySphereGeometry, skySphereMaterial );
        scene.add(skySphere);
    }

    /* 相机 */
    function initCamera() {
        camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 10000);
        camera.position.set(7, 5, 10);
        camera.lookAt(new THREE.Vector3(0, 0, 0));

    }

    /* 渲染器 */
    function initRender() {
        renderer = new THREE.WebGLRenderer({antialias: true});
        renderer.setSize(window.innerWidth-200, window.innerHeight);
        renderer.setClearColor(0xffffff);
        renderer.shadowMap.enabled = true;
        document.body.appendChild(renderer.domElement);

    }

    /* 灯光 */
    function initLight() {
        var planeGeometry = new THREE.PlaneGeometry(100,100,100,1);
        var texture = new THREE.TextureLoader().load("/static/img/public_img/1.png");
        var planeMaterial = new THREE.MeshLambertMaterial({map:texture});
        var plane = new THREE.Mesh(planeGeometry, planeMaterial);
        plane.rotation.x = -0.5*Math.PI;
        plane.name ='plane';
        plane.position.set(0,0,0);
        plane.receiveShadow = true;
        scene.add(plane);

        var ambiColor = "#ffffff";
        var ambientLight = new THREE.AmbientLight(ambiColor);//设置颜色
        scene.add(ambientLight);
        // //聚焦光源
        var pointColor = "#ffffff";
        var spotLight1 = new THREE.SpotLight(pointColor);
        spotLight1.position.set(-50, 60, 25);
        spotLight1.castShadow = true;
        spotLight1.shadow.camera.near = 20;
        spotLight1.shadow.camera.far = 500;
        spotLight1.shadow.camera.fov = 20;
        // spotLight1.target = plane;//光照照向地面
        spotLight1.distance = 0;
        spotLight1.intensity = 18;
        spotLight1.angle = 0.1;
        scene.add(spotLight1);
    }

    /* 控制器 */
    function initControls() {
        controls = new THREE.OrbitControls(camera, renderer.domElement);
		// 如果使用animate方法时，将此函数删除
		//controls.addEventListener( 'change', render );
		// 使动画循环使用时阻尼或自转 意思是否有惯性
		controls.enableDamping = true;
		//动态阻尼系数 就是鼠标拖拽旋转灵敏度
		controls.dampingFactor = 0.95;
		//是否可以缩放
		controls.enableZoom = true;
		//是否自动旋转
		//controls.autoRotate = true;
		//设置相机距离原点的最远距离
		controls.minDistance = 10;
		//设置相机距离原点的最远距离
		controls.maxDistance = 20;
		//是否开启右键拖拽
		controls.enablePan = false;
		//设置聚焦坐标
		// controls.target = new THREE.Vector3()
    }

    /* 调试插件 */
    function initGui() {
        guiControls = new function () {
            this.rotationSpeed = 0.01;
        };

        // let controls = new dat.GUI({width: 200});
        // controls.add(guiControls, 'rotationSpeed').listen();
    }

    /* 场景中的内容 */

    function initContent() {

        // 加载 glTF 格式的模型
        let loader = new THREE.GLTFLoader();/*实例化加载器*/

        loader.load('/static/models/CT/scene.gltf',function (obj) {
            obj.scene.name = 'zp';
            // console.log(obj.scene.children[0].children[0].children[0]);
            scene.add(obj.scene);
            document.getElementById('loading').style.display = 'none';


        },function (xhr) {

            console.log( ( xhr.loaded / xhr.total * 100 ) + '% loaded' );

        },function (error) {

            console.log('load error!'+error.getWebGLErrorMessage());

        })

    }

    /* 性能插件 */
    function initStats() {

        let stats = new Stats();

        document.body.appendChild(stats.domElement);

        return stats;

    }

    /* 窗口变动触发 */
    function onWindowResize() {

        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);

    }

    /* 数据更新 */
    function update() {

        // stats.update();

    }

    /* 初始化 */
    function init() {
        initScene();
        initCamera();
        initRender();
        initLight();
        initControls();
        initContent();
        initGui();
        /* 监听事件 */
        window.addEventListener('resize', onWindowResize, false);
    }

    /* 循环渲染 */
    function animate() {
        try{
            scene.getObjectByName('zp').rotation.y -= guiControls.rotationSpeed;
            // scene.getObjectByName('zp').position.x
            // scene.getObjectByName('plane').position.x += guiControls.rotationSpeed;
            // console.log(scene.getObjectByName('plane').position.x);
            if (scene.getObjectByName('plane').position.x > 7 ){
                scene.getObjectByName('plane').position.x = 0;
            }
            controls.target = new THREE.Vector3(scene.getObjectByName('zp').position.x,scene.getObjectByName('zp').position.y,scene.getObjectByName('zp').position.z)
            camera.lookAt(scene.getObjectByName('zp').position);

        }
        catch (e) {

        }
        requestAnimationFrame(animate);
        renderer.render(scene, camera);
        update();

    }

    /* 初始加载 */
    (function () {
        console.log("three init start...");

        init();
        animate();


        console.log("three init send...");
    })();

    function change_color(e) {
        var Color = {
            'black':[0,0,0],
            'white':[5,5,5],
            'gary':[1,1,1],
            'red': [5,0,0],
            'yellow':[5,5,0],
            'blue' :[0,0,5],
        };
        var name = e.getAttribute('name');
        try{
            for(var key in Color){
                if(name === key){
                    scene.getObjectByName('zp').children[0].children[0].children[0].children[16].material.color.r = Color[name][0];
                    scene.getObjectByName('zp').children[0].children[0].children[0].children[16].material.color.g = Color[name][1];
                    scene.getObjectByName('zp').children[0].children[0].children[0].children[16].material.color.b = Color[name][2];
                }
            }

        }
        catch (e) {

        }
    }