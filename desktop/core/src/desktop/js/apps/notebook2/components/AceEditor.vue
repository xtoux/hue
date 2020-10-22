<!--
  Licensed to Cloudera, Inc. under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  Cloudera, Inc. licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->

<template>
  <div :id="id" class="ace-editor" />
</template>

<script lang="ts">
  import ace from 'ext/aceHelper';
  import { UUID } from 'utils/hueUtils';
  import I18n from 'utils/i18n';
  import Vue from 'vue';
  import Component from 'vue-class-component';
  import { Prop } from 'vue-property-decorator';
  import { wrap } from 'vue/webComponentWrapper';

  @Component({
    methods: { I18n }
  })
  export default class AceEditor extends Vue {
    @Prop()
    value!: string;
    @Prop({ default: UUID() })
    id!: string;

    mounted(): void {
      this.$el.textContent = this.value;
      ace.edit(this.$el);
    }
  }

  export const COMPONENT_NAME = 'ace-editor';
  wrap(COMPONENT_NAME, AceEditor);
</script>
