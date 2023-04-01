import { createRouter, createWebHistory } from 'vue-router'
import HomeViewVue from '@/views/HomeView.vue'
import NoteViewVue from '@/views/NoteView.vue'
import FavoritesViewVue from '@/views/FavoritesView.vue'
import ToolBoxViewVue from '@/views/ToolBoxView.vue'
import NavigatorViewVue from '@/views/NavigatorView.vue'
import StorageViewVue from '@/views/StorageView.vue'
import AboutViewVue from '@/views/AboutView.vue'
import LoginViewVue from '@/views/LoginView.vue'
import UnFoundViewVue from '@/views/UnFoundView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeViewVue
    },
    {
      path: '/notes',
      name: 'notes',
      component: NoteViewVue
    },
    {
      path: '/favorites',
      name: 'favorites',
      component: FavoritesViewVue
    },
    {
      path: '/toolbox',
      name: 'toolbox',
      component: ToolBoxViewVue
    },
    {
      path: '/nav',
      name: 'navigator',
      component: NavigatorViewVue
    },
    {
      path: '/storage',
      name: 'storage',
      component: StorageViewVue
    },
    {
      path: '/about',
      name: 'about',
      component: AboutViewVue
    },
    {
      path: '/login',
      name: 'login',
      component: LoginViewVue
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: UnFoundViewVue
    },
  ]
})

export default router
