import { wrap } from 'vue/webComponentWrapper';
import AceEditor from './AceEditor.vue';

export const COMPONENT_NAME = 'hue-editor';
wrap(COMPONENT_NAME, AceEditor);


