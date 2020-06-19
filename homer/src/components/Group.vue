<template>
  <div class="group">
    <h3>
      {{ groupName }}
    </h3>

    <ul>
      <li>
        {{ preferredBudget }}
      </li>

      <li>
        {{ preferredSize }}
      </li>

      <li>
        {{ preferredRoomQuantity }}
      </li>

      <li>
        {{ preferredLocations }}
      </li>
    </ul>

    <span class="separator"/>

    <ul class="avatars">
      <li class="avatar">

      </li>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'Group',
  props: [
    'groupName',
    'users',
    'preferredBudget',
    'preferredSize',
    'preferredRoomQuantity',
    'preferredLocations'
  ]
}
</script>
