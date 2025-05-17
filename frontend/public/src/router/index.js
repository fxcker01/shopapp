import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import DeliveryView from '../views/DeliveryView.vue'
import ItemsView from '../views/ItemsView.vue'
import OrderView from '../views/OrderView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import ProfileView from '../views/ProfileView.vue'
import ItemDetail from '../views/ItemDetail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: { title: 'Головна — Меблевий магазин' }
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView,
      meta: { title: 'Про нас — Меблевий магазин' }
    },
    {
      path: '/delivery',
      name: 'delivery',
      component: DeliveryView,
      meta: { title: 'Доставка — Меблевий магазин' }
    },
    {
      path: '/items',
      name: 'items',
      component: ItemsView,
      meta: { title: 'Каталог товарів — Меблевий магазин' }
    },
    {
      path: '/order',
      name: 'order',
      component: OrderView,
      meta: { title: 'Оформлення замовлення — Меблевий магазин' }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      meta: { title: 'Вхід — Меблевий магазин' }
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView,
      meta: { title: 'Реєстрація — Меблевий магазин' }
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
      meta: { title: 'Профіль — Меблевий магазин' }
    },
    {
      path: '/item/:slug',
      name: 'item-detail',
      component: ItemDetail,
      meta: { title: 'Деталі товару — Меблевий магазин' }
    }
  ]
})

export default router;
