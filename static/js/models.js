let scene, camera, renderer, controls, guiControls;
    // let stats = initStats();

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
    camera.position.set(70, 50, 100);
    camera.lookAt(new THREE.Vector3(0, 0, 0));

}

/* 渲染器 */
function initRender() {

    renderer = new THREE.WebGLRenderer({antialias: true});
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setClearColor(0xffffff);
    renderer.shadowMap.enabled = true;
    document.body.appendChild(renderer.domElement);

}

/* 灯光 */
function initLight() {
    // var axes = new THREE.AxesHelper(20);
    // scene.add(axes);

    // var planeGeometry = new THREE.PlaneGeometry(200,200,100,1);
    // var texture = new THREE.TextureLoader().load("images/5.png");
    // var planeMaterial = new THREE.MeshLambertMaterial({map:texture});
    // var plane = new THREE.Mesh(planeGeometry, planeMaterial);
    // plane.rotation.x = -0.5*Math.PI;
    // plane.name ='plane';
    // plane.position.set(0,0,0);
    // plane.receiveShadow = true;
    // scene.add(plane);

    var ambiColor = "#ffffff";
    var ambientLight = new THREE.AmbientLight(ambiColor);//设置颜色
    scene.add(ambientLight);
    var pointColor = "#ffffff";
    var directionalLight = new THREE.DirectionalLight(pointColor);
    directionalLight.position.set(-50, 60, 200);
    directionalLight.castShadow = true;
    directionalLight.shadow.camera.near = 20;
    directionalLight.shadow.camera.far = 200;
    directionalLight.shadow.camera.left = -50;
    directionalLight.shadow.camera.right = 50;
    directionalLight.shadow.camera.top = 50;
    directionalLight.shadow.camera.bottom = -50;
    directionalLight.distance = 0;
    directionalLight.intensity = 5;
    directionalLight.shadow.mapSize.height = 1024;
    directionalLight.shadow.mapSize.width = 1024;
    scene.add(directionalLight);
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
    // controls.autoRotate = true;
    //设置相机距离原点的最远距离
    controls.minDistance = 70;
    //设置相机距离原点的最远距离
    controls.maxDistance = 250;
    //是否开启右键拖拽
    controls.enablePan = false;
    //设置聚焦坐标
    // controls.target = new THREE.Vector3()
}

/* 调试插件 */
function initGui() {

    guiControls = new function () {
        this.rotationSpeed = 0;
    };
}

/* 场景中的内容 */

function initContent() {

    // 加载 glTF 格式的模型
    let loader = new THREE.GLTFLoader();/*实例化加载器*/

    loader.load('/static/models/11/scene.gltf',function (obj) {
        obj.scene.name = 'zp';
        var car = obj.scene;
        console.log(car.children[0].children[0].children[0].children[0]);
        scene.add(car);
    },function (xhr) {

        console.log( ( xhr.loaded / xhr.total * 100 ) + '% loaded' );

    },function (error) {
        console.log(error)
        // console.log('load error!'+error.getWebGLErrorMessage());

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
window.onload = function() {
    var color = document.getElementsByClassName('color')[0];
    color.onchange = function(e){
        var change_thing = scene.getObjectByName('confirm');
        colors = change_thing.material.color;
        var hex = document.getElementsByClassName('color')[0].value;
        var c = hex_rgb(hex);
        colors.r = c[0];
        colors.g = c[1];
        colors.b = c[2];
    };
    function hex_rgb(hex){
        var r = parseInt(hex[1]+ hex[2],16)/255;
        var g = parseInt(hex[3]+ hex[4],16)/255;
        var b = parseInt(hex[5]+ hex[6],16)/255;
        return [r, g, b];
    }
    function get_hex(x){
        var e = parseInt(x*255).toString(16);
        var z = e;
        if (e === 0){
            z = '00';
        }
        if (e.length === 1){
            z = '0'+ e;
        }
        return z;
    }
    function rgb_hex(r, g, b){
        var result = '#'+ get_hex(r) + get_hex(g) + get_hex(b);
        return result;
    }

    var raycaster = new THREE.Raycaster();
    var	mouse = new THREE.Vector3();
    var canvas = document.getElementsByTagName('canvas')[0];
    canvas.addEventListener('click', onDocumentMouseClick, false);
    function onDocumentMouseClick(event) {
        event.preventDefault();
        //将鼠标点击位置的屏幕坐标转成threejs中的标准坐标,具体解释见代码释义
        mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
        mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
        //新建一个三维单位向量 假设z方向就是0.5
        //根据照相机，把这个向量转换到视点坐标系
        var vector = new THREE.Vector3(mouse.x, mouse.y, 0.5).unproject(camera);
        //在视点坐标系中形成射线,射线的起点向量是照相机， 射线的方向向量是照相机到点击的点，这个向量应该归一标准化。
        var raycaster = new THREE.Raycaster(camera.position, vector.sub(camera.position).normalize());
        //     //射线和模型求交，选中一系列直线
        var intersects = raycaster.intersectObjects(scene.children[3].children[0].children[0].children[0].children[0].children)[0].object;
        var car = scene.getObjectByName('zp').children[0].children[0].children[0].children[0].children;
        for(var i = 0 ;i < car.length; i++){
            car[i].name = '';
        }
        new_color = intersects.material.color;
        color.value = rgb_hex(new_color.r, new_color.g, new_color.b);
        intersects.name = 'confirm';
        // console.log(intersects)
    }
}