Hi! We develop web applications using the Laravel framework. We extensively use Livewire alongside various CSS libraries, primarily Bootstrap and Bulma. Recently, we’ve decided to adopt the Flux web component library, created by the same author as Livewire. Flux uses Tailwind CSS under the hood, integrates seamlessly with Livewire and AlpineJS, and addresses many accessibility concerns present in our current setup. It also simplifies tedious tasks, such as displaying validation errors.

Having successfully converted a few Laravel Blade templates to use Flux components and adopting the modern Laravel Blade component page layout, we’ve seen great results. However, with hundreds of Blade templates left to convert, we are looking for an automated process to streamline this transition.

Your task is to convert a provided Blade template that uses Bootstrap or Bulma into one using Flux components and Tailwind CSS. The converted template must adhere to the structure, functionality, and ‘house style’ we’ve adopted. This includes replacing Bootstrap or Bulma elements with their corresponding Flux/Tailwind components while maintaining functionality.

Below are examples of an original template and its converted version. These examples serve as a guide for the type of conversion we expect.

**Example 1:**

Original Blade template using Bulma CSS:

```blade
@extends('layouts.app')

@section('content')
<div class="container">
    <h3 class="title is-3">Make a Booking</h3>
    <form wire:submit.prevent="createBooking">
        <div class="columns">
            <div class="column">
                <div class="field">
                    <label class="label">Name</label>
                    <input wire:model.live="name" class="input" type="text" placeholder="Name">
                </div>
                @error('name')
                    <p class="help is-danger">{{ $message }}</p>
                @enderror
            </div>
            <div class="column">
                <div class="field">
                    <label class="label">Email</label>
                    <input wire:model.live="email" class="input" type="email" placeholder="Email">
                </div>
                @error('email')
                    <p class="help is-danger">{{ $message }}</p>
                @enderror
            </div>
        </div>
        <hr />
        <button type="submit" class="button is-primary">Create Booking</button>
    </form>
</div>
@endsection
```

Converted template using Tailwind CSS and Flux components:

```blade
<x-layout>
    <flux:heading>Make a Booking</flux:heading>
    <div class="flex gap-6">
        <flux-form wire:submit.prevent="createBooking">
            <flux:input wire:model.live="name" label="Name" />
            <flux:input wire:model.live="email" label="Email" />

            <flux:separator />

            <flux:button type="submit">Create Booking</flux:button>
        </flux-form>
    </div>
</x-layout>
```

Please ensure the converted template preserves the original layout and features while fully leveraging the capabilities of Flux components. Consistency with the provided example conversions is key.

You should respond with only the converted template, no other text or comments.  If you feel it is important to add any additional comments, please add them to the end of the template inside html comment block so that the response is still valid html.
