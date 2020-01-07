import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/',
      component: () => import(/* webpackChunkName: "home" */ '../components/Home.vue'),
      meta: {title: 'home'},
      children: [
        {
          path: '/home',
          component: () => import('../components/404.vue'),
          meta: {title: '首页'}
        },
        {
          path: '/requisition',
          component: () => import(/* webpackChunkName: "请购" */ '../components/purchase/req_pur/ReqPurCheck.vue'),
          meta: {title: '请购单'}
        },
        {
          path: '/sell',
          component: () => import('../components/sell/SellCheck.vue'),
          meta: {title: '销售订单'}
        },
        {
          path: '/constract',
          component: () => import('../components/purchase/contract/PurConCheck'),
          meta: {title: '采购合同'}
        },
        {
          path: '/purchase',
          component: () => import('../components/purchase/order/PurOrdCheck'),
          meta: {title: '采购订单'}
        },
        {
          path: '/buyinstore',
          component: () => import('../components/store/in_store/buy_in_store/BisCheck'),
          meta: {title: '采购入库'}
        },
        {
          path: '/organizationmanage',
          component: () => import(/* webpackChunkName: "donate" */ '../components/system/OrganizationManage.vue'),
          meta: {title: '组织架构管理'}
        },
        {
          path: '/rolemanage',
          component: () => import(/* webpackChunkName: "donate" */ '../components/system/RoleManage.vue'),
          meta: {title: '角色管理'}
        },
        {
          path: '/usermanage',
          component: () => import(/* webpackChunkName: "donate" */ '../components/system/UserManage.vue'),
          meta: {title: '用户管理'}
        },
        {
          path: '/organization',
          component: () => import(/* webpackChunkName: "donate" */ '../components/basic_data/Organization.vue'),
          meta: {title: '库存组织管理'}
        },
        {
          path: '/center',
          component: () => import(/* webpackChunkName: "donate" */ '../components/basic_data/Center.vue'),
          meta: {title: '中心管理'}
        },
        {
          path: '/brand',
          component: () => import(/* webpackChunkName: "donate" */ '../components/basic_data/Brand.vue'),
          meta: {title: '品牌管理'}
        },
        {
          path: '/warehouse',
          component: () => import(/* webpackChunkName: "donate" */ '../components/basic_data/warehouse.vue'),
          meta: {title: '仓库维护'}
        },
        {
          path: '/supplier',
          component: () => import(/* webpackChunkName: "donate" */ '../components/basic_data/Supplier.vue'),
          meta: {title: '供应商维护'}
        },
        {
          path: '/customer',
          component: () => import(/* webpackChunkName: "donate" */ '../components/basic_data/Customer.vue'),
          meta: {title: '客户维护'}
        },
        {
          path: '/meterage',
          component: () => import(/* webpackChunkName: "donate" */ '../components/basic_data/Meterage.vue'),
          meta: {title: '计量单位维护'}
        },
        {
          path: '/materialtype',
          component: () => import(/* webpackChunkName: "donate" */ '../components/basic_data/MaterialType.vue'),
          meta: {title: '物料类别维护'}
        },
        {
          path: '/material',
          component: () => import(/* webpackChunkName: "donate" */ '../components/basic_data/Material.vue'),
          meta: {title: '物料维护'}
        },
        {
          path: '/stockcheck',
          component: () => import(/* webpackChunkName: "donate" */ '../components/store/stock/StockCheck.vue'),
          meta: {title: '库存量查询'}
        },
        {
          path: '/stockrequisition',
          component: () => import(/* webpackChunkName: "donate" */ '../components/store/stock_adjustment/stock_require/TransferRequest.vue'),
          meta: {title: '转库申请单'}
        },
        {
          path: '/stockchange',
          component: () => import(/* webpackChunkName: "donate" */ '../components/store/stock_adjustment/stock_transfer/ChangeCheck.vue'),
          meta: {title: '转库单'}
        },
        {
          path: '/stockconfirm',
          component: () => import(/* webpackChunkName: "donate" */ '../components/store/stock_adjustment/stock_confirm/ConfirmCheck.vue'),
          meta: {title: '库存盘点'}
        },
        {
          path: '/stockbegin',
          component: () => import(/* webpackChunkName: "donate" */ '../components/store/stock_adjustment/stock_begin/BeginCheck.vue'),
          meta: {title: '期初库存'}
        }
      ]
    },
    {
      path: '/login',
      component: () => import(/* webpackChunkName: "login" */ '../components/Login.vue'),
      meta: {title: '登录'}
    },
    {
      path: '*',
      component: () => import(/* webpackChunkName: "404" */ '../components/404.vue'),
      meta: {title: '404'}
    }
  ]
})
